def my_function(nama_depan, nama_akhir=""):
    print("Hello {} - {}".format (nama_depan, nama_akhir))

my_function("Khulud", "Saekhan")
my_function("Anisya", "Salsabila")
my_function("Joice")

# function in keywords
def my_function2 (child3, child2, child1):
    print("The youngest child is " + child3)

my_function2(child1 = "Regie", child2 = "Cyn", child3 = "Meta")
my_function2("Regie", "Cyn", "Meta")