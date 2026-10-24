package cl.duoc.biblioteca.service;
import cl.duoc.biblioteca.model.Libro;
import org.springframework.stereotype.Service;
//import java.util.ArrayList;
import java.util.List;
// se importa la clase LibroRepository para poder utilizarla en la clase LibroService y acceder a los métodos de la capa de persistencia de datos.
import cl.duoc.biblioteca.repository.LibroRepository;

    // Service indica que esta clase es un servicio de Spring y puede ser inyectada en otras clases
    // La anotación @Service es una especialización de @Component, lo que significa que esta clase será detectada automáticamente por Spring durante el escaneo de componentes y se registrará como un bean en el contexto de la aplicación
    // La anotación @Service también puede ser utilizada para aplicar aspectos de programación orientada a aspectos (AOP) a los métodos de esta clase, como transacciones, seguridad, etc.

    // Las Listas son una estructura de datos que permite almacenar una colección de elementos, en este caso objetos de tipo Libro. La implementación ArrayList es una lista dinámica que permite agregar, eliminar y acceder a elementos de manera eficiente.
    // La lista libros se inicializa como una nueva instancia de ArrayList, lo que significa que estará vacía al inicio y se podrán agregar libros a medida que se necesite.
    // Las listas almacenan la referencia de los objetos, lo que significa que si se modifica un objeto en la lista, se modificará el objeto original. Esto es importante tenerlo en cuenta al trabajar con listas de objetos.
    // las referencias de los objetos en la lista se almacenan en memoria, por lo que si se elimina un objeto de la lista, se eliminará la referencia a ese objeto, pero el objeto en sí seguirá existiendo en memoria hasta que no haya más referencias a él y sea recolectado por el recolector de basura de Java.
    // Este almacenamiento de referencias permite que los objetos sean compartidos entre diferentes partes del programa, lo que puede ser útil para evitar duplicación de datos y mejorar la eficiencia del programa.
    // A diferencia de Libro libro = new Libro(); el cuál va cambiando de valor, la lista libros almacena referencias a los objetos Libro, lo que significa que si se modifica un objeto en la lista, se modificará el objeto original. Esto es importante tenerlo en cuenta al trabajar con listas de objetos.
    // Libro libro = new Libro(); va cambiando referencia a un nuevo objeto, por lo que se pierde la referencia al objeto original y no se puede acceder a él, en cambio, la lista no pierde la referencia a los objetos que contiene, por lo que se puede acceder a ellos en cualquier momento mientras existan referencias a ellos en la lista.

    // La clase LibroService es un servicio que se encargará de manejar la lógica de negocio relacionada con los libros, como agregar, eliminar, buscar y actualizar libros en la lista libros.
    @Service
    public class LibroService {
        private final LibroRepository repository;
        public LibroService(LibroRepository repository) {
            this.repository = repository;
        }

        //private List<Libro> libros =
                //new ArrayList<>();



        // Se crea la lista, pero nadie puede usarla aún, ya que no hay métodos públicos para acceder a ella. 
        // Esto es una buena práctica de encapsulamiento, ya que se protege la lista de modificaciones externas y se asegura que solo la clase LibroService pueda manipularla.


        // METODOS 
        // METODOS CRUD (Create, Read, Update, Delete)
        // Recibe un objeto Libro como parámetro.
        // Este método puede ser invocado desde el controlador
        // después de que Spring convierta el JSON recibido en un objeto Libro mediante @RequestBody.
        // Y lo agrega a la lista libros gracias a la implementación de ArrayList y su método add().
        // Luego, devuelve el mismo objeto Libro que se agregó a la lista.
        // Esto permite que el método pueda ser utilizado para agregar libros a la lista y también para obtener una referencia al libro agregado, si es necesario.
        // AGREGACIÓN DE LIBRO (POST)
        public Libro agregarLibro(Libro libro){
            return repository.save(libro);

            //libros.add(libro);
            //return libro;
        }


        // OBTENCIÓN DE LIBROS (GET)
        // El método obtenerTodos devuelve la lista completa de libros almacenados en la lista libros.
        //
        public List<Libro> obtenerTodos(){
            return repository.findAll();

            //return libros;
        }


        //  OBTENCIÓN DE LIBRO POR ID (GET)
        // El método obtenerPorId recibe un parámetro de tipo Long que representa el id del libro
        // y busca en la lista libros un libro que tenga el mismo id.
        // Si encuentra un libro con el mismo id, lo devuelve. Si no lo encuentra, devuelve null.
        // Libro obtenerPorId(Long id){

        public Libro obtenerPorId(Long id){
            return repository.findById(id)
                    .orElse(null);
        

            //for (Libro libro : libros) {

                //if (libro.getId().equals(id)) {
                    //return libro;
                //}

            //}

            //return null;
        }


        // ACTUALIZACIÓN DE LIBRO (PUT)
        // El método actualizarLibro recibe un objeto Libro como parámetro y busca en la lista libros un libro que tenga el mismo id.
        // Si encuentra un libro con el mismo id, actualiza sus atributos con los valores del objeto
        public Libro actualizarLibro(Long id, Libro libroActualizado) {

            Libro libro = repository.findById(id)
                    .orElse(null);

            if (libro != null) {

                libro.setTitulo(
                        libroActualizado.getTitulo());

                libro.setAutor(
                        libroActualizado.getAutor());

                libro.setAnioPublicacion(
                        libroActualizado.getAnioPublicacion());

                libro.setGenero(
                        libroActualizado.getGenero());

                return repository.save(libro);
            }

            return null;
        

            //for (Libro libro : libros) {

                //if (libro.getId().equals(id)) {

                    //libro.setTitulo(
                            //libroActualizado.getTitulo());

                    //libro.setAutor(
                            //libroActualizado.getAutor());

                    //libro.setAnioPublicacion(
                            //libroActualizado.getAnioPublicacion());

                    //libro.setGenero(
                            //libroActualizado.getGenero());

                    //return libro;
                //}
            //}

            //return null;
        }

        // ELIMINACIÓN DE LIBRO (DELETE)
        // El método eliminarLibro recibe un parámetro de tipo Long que representa el id del libro
        // y busca en la lista libros un libro que tenga el mismo id.
        // Si encuentra un libro con el mismo id, lo elimina de la lista y devuelve true. Si no lo encuentra, devuelve false.
        public Libro eliminarLibro(Long id){

            Libro libro = repository.findById(id)
                    .orElse(null);

            if(libro != null){
                repository.deleteById(id);
            }

            return libro;


        //for (Libro libro : libros) {

            //if (libro.getId().equals(id)) {

                //libros.remove(libro);

                //return libro;
            //}
        //}

            //return null;
        }


}       