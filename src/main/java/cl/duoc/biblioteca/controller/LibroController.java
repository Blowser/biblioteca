package cl.duoc.biblioteca.controller;
import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import cl.duoc.biblioteca.model.Libro;

import org.springframework.web.bind.annotation.RequestMapping;
import cl.duoc.biblioteca.service.LibroService;


// Import para darle el estado deseado a las respuestas
// codigo 200 OK, codigo 404 Not Found, codigo 500 Internal Server Error, etc.
// ANTES:
// public Libro obtenerPorId(...)
//
// DESPUÉS:
// public ResponseEntity<Libro> obtenerPorId(...)
//
// El cambio permite devolver códigos HTTP apropiados
// además de los datos del recurso solicitado.
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;



// RestController Indica que la clase es un controlador de Spring MVC y que los métodos de esta clase manejarán solicitudes HTTP y devolverán respuestas HTTP.
// Indica que una clase expone endpoints HTTP y puede responder solicitudes REST.
// Un endpoint es una ruta HTTP asociada a un verbo HTTP específico (GET, POST, PUT o DELETE)
// que permite interactuar con un recurso expuesto por la API.
// Exponer endpoints significa hacer que ciertos métodos de la clase estén disponibles para ser llamados a través de solicitudes HTTP desde clientes externos, como navegadores web o aplicaciones móviles.
// Postman es una herramienta que permite probar y consumir APIs RESTful, enviando solicitudes HTTP a los endpoints expuestos por la aplicación y visualizando las respuestas recibidas.
// RequestMapping Especifica la ruta base para todos los endpoints definidos en la clase. En este caso, todos los endpoints estarán bajo la ruta "/libros".
// RequestMapping se suele basar en el modelo o entidad que representa la clase. En este caso, la clase LibroController está relacionada con la entidad "Libro", por lo que se utiliza "/libros" como ruta base para los endpoints relacionados con libros.
@RestController
@RequestMapping("/libros")
public class LibroController {
    
    // ============================
    // INYECCIÓN DE DEPENDENCIAS
    // ============================

    // LibroController necesita utilizar los métodos de LibroService,
    // pero no crea la instancia manualmente mediante:
    //
    // LibroService service = new LibroService();
    //
    // En su lugar, Spring crea y administra el objeto LibroService
    // gracias a la anotación @Service.
    //
    // Cuando Spring crea LibroController, inyecta automáticamente
    // una referencia a LibroService mediante el constructor.
    //
    // Esto permite separar responsabilidades:
    //
    // Controller
    // ↓
    // Service
    //
    // El Controller recibe solicitudes HTTP.
    // El Service contiene la lógica de negocio.

    // private:
    // La variable sólo puede ser utilizada dentro de LibroController.
    //
    // final:
    // La referencia no puede apuntar a otro LibroService una vez asignada.
    // Esto evita reasignaciones accidentales y asegura que el controlador
    // utilice siempre la misma instancia entregada por Spring.
    private final LibroService service;

    
    // Spring llama automáticamente a este constructor e inyecta
    // la instancia de LibroService que administra.
    //
    // Conceptualmente ocurre algo parecido a:
    //
    // LibroService service = new LibroService();
    // LibroController controller = new LibroController(service);
    // Pero todo esto lo hace Spring de forma automática.

    // public LibroController es el constructor de la clase LibroController.
    // este constructor recibe un parámetro de tipo LibroService llamado service.
    // this.service = service asigna la referencia del parámetro service a la variable de instancia service de la clase LibroController.
    // Guarda la referencia recibida para que los métodos del
    // controlador puedan utilizar el servicio posteriormente.

    public LibroController(
            LibroService service) {
            // El constructor de la clase LibroController recibe una instancia de LibroService como parámetro y la asigna a la variable de instancia service. 
            // Esto permite que el controlador pueda utilizar los métodos del servicio para realizar operaciones relacionadas con los libros.

        this.service = service;
    }

    // GetMapping Asocia un método Java a solicitudes HTTP GET. 
    // Se utiliza para obtener información o consultar recursos.

    //TEST DE ENDPOINTS
    @GetMapping("/test")
    public String probar() {
        return "Controlador Libro funcionando";
    }

    // FUNCIONES CRUD

    // OBTENER TODOS LOS LIBROS Y POR ID
    //PathVariable Obtiene valores enviados dentro de la ruta URL y los convierte en parámetros del método.
    //// Ejemplo:
    // GET /libros/15
    // @PathVariable Long id
    // id = 15
    
    @GetMapping
    public List<Libro> obtenerTodos() {

        // devuelve una respuesta HTTP con el estado 200 OK y el cuerpo de la respuesta contiene la lista de libros obtenida del servicio.
        return service.obtenerTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Libro> obtenerPorId(
            @PathVariable Long id) {

        Libro libro = service.obtenerPorId(id);

        if (libro != null) {
            //devuelve una respuesta HTTP con el estado 200 OK y el cuerpo de la respuesta contiene el libro encontrado.
            return ResponseEntity.ok(libro);
        }
        // Si el libro no se encuentra, devuelve una respuesta HTTP con el estado 404 Not Found y un cuerpo vacío.
        return ResponseEntity.notFound().build();
    }

    // CREAR LIBRO
    //PostMapping Asocia un método Java a solicitudes HTTP POST.
    //Se utiliza para enviar datos al servidor y crear nuevos recursos.
    //RequestBody convierte automáticamente el cuerpo de una solicitud HTTP en un objeto Java.
    @PostMapping
    public ResponseEntity<Libro> crearLibro(
            @RequestBody Libro libro) {

        Libro nuevoLibro =
                service.agregarLibro(libro);
        // devuelve una respuesta HTTP con el estado 201 Created y el cuerpo de la respuesta contiene el libro recién creado.        
        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(nuevoLibro);
    }

    // ACTUALIZAR LIBRO
    //PutMapping Asocia un método Java a solicitudes HTTP PUT.
    // Se utiliza para actualizar recursos existentes.
    // Obtiene el ID desde la URL y recibe los nuevos datos desde el cuerpo de la solicitud.
    @PutMapping("/{id}")
    public ResponseEntity<Libro> actualizarLibro(
            @PathVariable Long id,
            @RequestBody Libro libro) {

        Libro actualizado =
                service.actualizarLibro(id, libro);

        if (actualizado != null) {
            // devuelve una respuesta HTTP con el estado 200 OK y el cuerpo de la respuesta contiene el libro actualizado.
            return ResponseEntity.ok(actualizado);
        }
        // Si el libro no se encuentra, devuelve una respuesta HTTP con el estado 404 Not Found y un cuerpo vacío.
        return ResponseEntity.notFound().build();
    }

    // ELIMINAR LIBRO
    //DeleteMapping Asocia un método Java a solicitudes HTTP DELETE.
    // Se utiliza para eliminar recursos existentes.
    // Obtiene el ID desde la URL y realiza la eliminación del recurso correspondiente.
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarLibro(
            @PathVariable Long id) {

        Libro libro = service.eliminarLibro(id);

        if (libro != null) {
            // devuelve una respuesta HTTP con el estado 204 No Content, indicando que la eliminación fue exitosa y no hay contenido adicional que devolver.
            return ResponseEntity.noContent().build();
        }
        // Si el libro no se encuentra, devuelve una respuesta HTTP con el estado 404 Not Found y un cuerpo vacío.
        return ResponseEntity.notFound().build();
    }




}