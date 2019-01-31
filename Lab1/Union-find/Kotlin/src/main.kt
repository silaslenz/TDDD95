import java.util.StringTokenizer
import java.io.BufferedReader
import java.io.BufferedOutputStream
import java.io.IOException
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintWriter
import java.io.OutputStream

internal class Kattio : PrintWriter {

    val int: Int
        get() = Integer.parseInt(nextToken()!!)

    val double: Double
        get() = java.lang.Double.parseDouble(nextToken()!!)

    val long: Long
        get() = java.lang.Long.parseLong(nextToken()!!)

    val word: String?
        get() = nextToken()


    private var r: BufferedReader? = null
    private var line: String? = null
    private var st: StringTokenizer? = null
    private var token: String? = null

    constructor(i: InputStream) : super(BufferedOutputStream(System.out)) {
        r = BufferedReader(InputStreamReader(i))
    }

    constructor(i: InputStream, o: OutputStream) : super(BufferedOutputStream(o)) {
        r = BufferedReader(InputStreamReader(i))
    }

    fun hasMoreTokens(): Boolean {
        return peekToken() != null
    }

    private fun peekToken(): String? {
        if (token == null)
            try {
                while (st == null || !st!!.hasMoreTokens()) {
                    line = r!!.readLine()
                    if (line == null) return null
                    st = StringTokenizer(line!!)
                }
                token = st!!.nextToken()
            } catch (e: IOException) {
            }

        return token
    }

    private fun nextToken(): String? {
        val ans = peekToken()
        token = null
        return ans
    }
}

var parent: IntArray = IntArray(0)


fun main(args: Array<String>) {
    val io = Kattio(System.`in`, System.`out`);
//    var line = readLine()!!.split(" ");
    val N = io.int
    val Q = io.int
    parent = IntArray(N) { -1 }
    val sb = StringBuilder()
    for (i in 0 until Q) {
//        println(line)
        val op = io.word!![0]
        val a = io.int
        val b = io.int
//        io.println(op)
//        io.println(a)
//        io.println(b)
        if ('=' == op) {
            merge(a, b)
        } else {
            if (is_in_same(a, b)) {
                sb.append("yes\n")
            } else {
                sb.append("no\n")
            }
        }
    }
    io.print(sb.toString())
    io.close()
}


fun get_root(a: Int): Int {
    var root = a;
    while (parent[root] != root && parent[root]!=-1)
        root = parent[root]
    return root
}

fun is_in_same(a: Int, b: Int): Boolean {
//    println(a)
//    println(b)
    return get_root(a) == get_root(b)
}

fun merge(a: Int, b: Int) {
    if (a == b)
        return
    val root_of_a = get_root(a)
    val root_of_b = get_root(b)
    if (root_of_a == root_of_b)
        return
    if (root_of_a < root_of_b)
        parent[root_of_a] = root_of_b
    else
        parent[root_of_b] = root_of_a
}