package cl.duoc.biblioteca.model;
import jakarta.persistence.*;
// se importa jakarta.persistence.* para poder utilizar las anotaciones de JPA (Java Persistence API) que permiten mapear la clase Libro a una tabla de base de datos.
// se implementa @Entity para indicar que la clase Libro es una entidad de JPA y será mapeada a una tabla de base de datos.
// se importa @Table para indicar el nombre de la tabla de base de datos a la que se mapeará la clase Libro.
@Entity
@Table(name = "LIBROS")
public class Libro {

    // ============================
    // GETTERS Y SETTERS
    // ============================
    //
    // Los atributos de la clase son privados (private),
    // por lo que no pueden ser accedidos directamente
    // desde otras clases.
    //
    // Los getters permiten obtener (leer) el valor
    // de un atributo.
    //
    // Los setters permiten modificar (actualizar)
    // el valor de un atributo.
    //
    // Esto forma parte del principio de encapsulación
    // de la Programación Orientada a Objetos (POO).

    // se implementa @Id para indicar que el atributo id es la clave primaria de la entidad Libro.
    // se implementa @GeneratedValue para indicar que el valor del atributo id será generado automáticamente por la base de datos.
    // se implementa @Column para indicar el nombre de la columna de la tabla de base de datos a la que se mapeará el atributo id.
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private Long id;

    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }
    public Integer getAnioPublicacion() {
        return anioPublicacion;
    }
    public void setAnioPublicacion(Integer anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }
    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }

    // se implementa nullable = false para indicar que los atributos titulo, autor, anioPublicacion y genero no pueden ser nulos en la base de datos.
    @Column(name = "TITULO", nullable = false)
    private String titulo;
    @Column(name = "AUTOR", nullable = false)
    private String autor;
    @Column(name = "ANIO_PUBLICACION", nullable = false)
    private Integer anioPublicacion;
    @Column(name = "GENERO", nullable = false)
    private String genero;

    // Constructor vacío requerido por JPA
    public Libro() {
    }
}
