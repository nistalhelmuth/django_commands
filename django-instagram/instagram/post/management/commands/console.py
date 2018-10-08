from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from post.models import Post, UserLikePost





class Command(BaseCommand):
    def handle(self, *args, **kwargs):
      flag = True
      while (flag):
        print("---------------------")
        print("1.Crear usuario")
        print("2.Lista usuarios")
        print("3.Acceder")
        print("4.Salir")
        ans = input("Ingrese la opción que se desea")

        #crear un usuario
        if(ans == '1'):
          nombre=input("Ingrese nombre: ")
          apellido=input("Ingrese apellido: ")
          email=input("Ingrese email: ")
          username=input("Ingrese username: ")
          try:
            new_user = User(username=username,first_name=nombre,last_name=apellido,email=email,password="")
            new_user.save()
            print("Usuario creado!")
          except Exception as e:
            print("Usuario no creado")

        elif(ans == '2'):
          registered_users = User.objects.all()
          if (len(registered_users)>0):
            for user in registered_users:
              print("pk={}: {} - {}".format(user.pk, user.first_name, user.email))
          else:
            print("no hay users registrados")

        elif(ans == '3'):
          email=input("Ingrese email: ")
          username=input("Ingrese username: ")
          try:
            user = User.objects.get(email=email, username= username)
            print("Bienvenido {}!".format(user.first_name))
            flag2 = True
            while (flag2):
              print("---------------------")
              print("Que quieres hacer {}?".format(user.first_name))
              print("1.Crear post")
              print("2.Me gusta post")
              print("3.Eliminar post")
              print("4.Regresar")
              ans2 = input("Ingrese la opción que deceas: ")

              if(ans2 == '1'):
                titulo=input("Ingresa titulo: ")
                contenido=input("Ingresa contenido: ")
                post = Post(owner=user,title=titulo, content=contenido)
                post.save()
                print("Post creado")

              elif(ans2 == '2'):
                registered_posts = Post.objects.all()
                if (len(registered_posts)>0):
                  for post in registered_posts:
                    likes=UserLikePost.objects.filter(post=post.pk).count()
                    print("pk={}: {} ({})\n {} \n".format(post.pk, post.title, likes, post.content))
                  primary_k=input("Ingrese la llave primaria que del post que le gusta: ")
                  try:
                    post = Post.objects.get(pk=primary_k)
                    userlike = UserLikePost(user=user,post=post)
                    userlike.save()
                    print("Me gusta registrado")
                  except Exception as e:
                    print("Post no encontrado")
                else:
                  print("No hay post")
                  
              elif(ans2 == '3'):
                print("Estos son tus post:")
                user_posts = Post.objects.filter(owner= user.pk)
                if(len(user_posts)>0):
                  for post in user_posts:
                    likes=UserLikePost.objects.filter(post=post.pk).count()
                    print("pk={}: {} ({})\n {} \n".format(post.pk, post.title, likes, post.content))
                  primary_k=input("Ingrese la llave primaria del post que va a borrar: ")
                  try:
                    post = Post.objects.get(pk=primary_k)
                    post.delete()
                    print("Post eliminado")
                  except Exception as e:
                    print("Post no encontrado")
                else:
                  print("no hay post")

              elif(ans2 == '4'):
                print("hasta luego {}!".format(user.first_name))
                flag2=False
              else:
                print("opcion invalida")

          except Exception as e:
            print("El usuario no esta registrado")
          
        elif(ans == '4'):
          flag = False
        else:
          print("opción inválida")
      print("Apagado.")


