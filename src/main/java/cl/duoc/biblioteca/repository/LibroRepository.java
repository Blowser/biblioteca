package cl.duoc.biblioteca.repository;

// se importa org.springframework.data.jpa.repository.JpaRepository para poder 
// utilizar la interfaz JpaRepository que permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre la entidad Libro.
// se importa cl.duoc.biblioteca.model.Libro para poder utilizar la clase Libro 
// que representa la entidad de la base de datos.
import org.springframework.data.jpa.repository.JpaRepository;
import cl.duoc.biblioteca.model.Libro;

// se implementa la interfaz LibroRepository que extiende de JpaRepository<Libro, Long> 
// para poder realizar operaciones CRUD sobre la entidad Libro.
public interface LibroRepository
        // implementa JpaRepository<Libro, Long> para poder realizar operaciones CRUD sobre la entidad Libro.
        // reduce la cantidad de código que se debe escribir para implementar un repositorio de datos, 
        // ya que JpaRepository proporciona métodos predefinidos para realizar operaciones CRUD y consultas personalizadas.
        // facilita el uso de la base de datos, ya que JpaRepository se encarga de manejar la conexión y las transacciones con la base de datos.
        extends JpaRepository<Libro, Long> {
}
