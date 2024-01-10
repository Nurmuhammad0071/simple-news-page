from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # print(request.META['sasas'])
    html = """
    <div style='width=100%;height:50px;background-color:#555'>
    <a href='http://127.0.0.1:8000/about'>kirish</a>
    </div>
    """
    return HttpResponse(html)


def about(request):
    # print(request.META['sasas'])
    # html = """
    # <div style='width=100%;height:50px;background-color:red'>
    #
    # </div>
    # """
    html = f"""
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Yangiliklar Sahifasi</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Yangiliklar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Bosh Sahifa <span class="sr-only">(hozirgi)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Yangiliklar</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Kategoriyalar</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Biz haqimizda</a>
            </li>
        </ul>
    </div>
</nav>

<!-- Header -->
<div class="jumbotron jumbotron-fluid text-center bg-primary text-white">
    <div class="container">
        <h1 class="display-4">So'nggi yangiliklar</h1>
        <p class="lead">Eng so'nggi vaqtincha xabarlarni ko'rib chiqing.</p>
    </div>
</div>

<!-- Main Content -->
<div class="container mt-4">
    <div class="row">
        <!-- News Cards -->
        <div class="col-lg-8">
            <div class="card mb-4">
                <img src="https://placehold.it/800x400" class="card-img-top" alt="Yangilik rasmi">
                <div class="card-body">
                    <h2 class="card-title">Eng katta yangilik</h2>
                    <p class="card-text">Bu birinchi yangilik matni bo'ladi. Batafsil ma'lumot uchun bog'laning.</p>
                    <a href="#" class="btn btn-primary">Batafsil</a>
                </div>
            </div>

            <!-- Add more cards as needed -->

        </div>

        <!-- Sidebar -->
        <div class="col-lg-4">
            <div class="card mb-4">
                <div class="card-body">
                    <h5 class="card-title">So'nggi xabarlar</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><a href="#">Xabar 1</a></li>
                        <li class="list-group-item"><a href="#">Xabar 2</a></li>
                        <li class="list-group-item"><a href="#">Xabar 3</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Footer -->
<footer class="bg-dark text-white py-3 text-center">
    &copy; 2024 Yangiliklar Sahifasi. Barcha huquqlar himoyalangan.
</footer>

<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>

    """

    return HttpResponse(html)
