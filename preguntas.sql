-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-03-2024 a las 17:03:42
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `encuesta`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preguntas`
--

CREATE TABLE `preguntas` (
  `id` int(10) UNSIGNED NOT NULL,
  `pregunta` varchar(150) NOT NULL,
  `estatus` int(2) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `preguntas`
--

INSERT INTO `preguntas` (`id`, `pregunta`, `estatus`) VALUES
(1, ' \"Tengo fama de decir lo que pienso claramente y sin rodeos.\"', 1),
(2, '\"Estoy seguro(a) de lo que es bueno y lo que es malo, lo que esta bien y lo que está mal\".', 1),
(3, ' \"Muchas veces actuó sin mirar las consecuencias\".', 1),
(4, ' \"Normalmente trato de resolver los problemas metódicamente y paso a paso.\"', 1),
(5, '\"Creo que los formulismos acortan y limitan la actuación libre de las personas.\"', 1),
(6, ' \"Me interesa saber cuáles son los sistemas de valores de los demás u con qué criterios actúan.\"', 1),
(7, '\"Pienso que el actuar intuitivamente puede ser siempre tan válido como actuar reflexivamente.\"', 1),
(8, ' \"Creo que lo más importante es que las cosas funcionen.\"', 1),
(9, ' \"Procuro estar al tanto de lo que ocurre aqui y ahora.\"', 1),
(10, '\"Disfruto cuando tengo tiempo para preparar mi trabajo y realizarlo a conciencia.\"', 1),
(11, '\"Estoy a gusto siguiendo un orden, en las comidas, en el estudio , haciendo ejercicio regularmente.\"', 1),
(12, '\"Cuando esucho una nueva idea, enseguida comienzo a pensar cómo ponerla en práctica.\"', 1),
(13, ' \"Prefiero las ideas originales y novedosas aunque no sean prácticas.\"', 1),
(14, ' \"Admito y me ajusto a las normas sólo si me sirven para lograr mis objetivos.\"', 1),
(15, '\"Normalmente encajo bien con personas reflexivas, y me cuesta sintonizar con personas demasiadas espontáneas, imprevisibles.\"', 1),
(16, ' \"Escucho  con más frecuencia de lo que hablo.\"', 1),
(17, '\"Prefiero las cosas estructuradas a las desordenadas.\"', 1),
(18, ' \"Cuando poseo cualquier información, trato de interpretarla bien antes de manifestar alguna conclusión\"', 1),
(19, ' \"Antes de hacer algo estudio con cuidado sus ventajas e inconvenientes.\"', 1),
(20, '\"Crezco con el reto de hacer algo nuevo y diferente.\"', 1),
(21, '\"Casi siempre procuro ser coherente con mis criterios y sistemas de valores.Tengo principios y los sigo.\"', 1),
(22, '\"Cuando hay una discusión no me gusta ir con rodeos.\"', 1),
(23, '\"Me disgusta implicarme afectivamente en mi ambiente de trabajo. Prefiero mantener relaciones distantes.\"', 1),
(24, '\"Me gustan más las personas realistas y concretas que las teóricas.\"', 1),
(25, '\"Me cuesta ser creativo(a),romper estructuras.\"', 1),
(26, '\"Me siento a gusto con personas espontáneas y divertidas.\"', 1),
(27, '\"La mayoría de las veces expreso abiertamente cómo me siento.\"', 1),
(28, '\"Me gusta analizar y dar vueltas a las cosas.\"', 1),
(29, '\"Me molesta que la gente no se tome en serio las cosas.\"', 1),
(30, '\"Me atrae experimentar y practicar las últimas técnicas y novedades.\"', 1),
(31, '\"Soy cauteloso(a) a la hora de sacar conclusiones.\"', 1),
(32, '\"Prefiero contar con el mayor número de fuentes de información. Cuantos más datos se reúnan para reflexionar, mejor.\"', 1),
(33, '\"Tiendo a ser perfeccionista.\"', 1),
(34, '\"Prefiero oír las opiniones de los demás antes de exponer la mía.\"', 1),
(35, '\"Me gusta afrontar la vida espontáneamente y no tener que planificar todo previamente.\"', 1),
(36, '\"En las discusiones me gusta observar cómo actúan los demás participantes.\"', 1),
(37, '\"Me siento incómodo(a) con las personas calladas y demasiado analíticas.\"', 1),
(38, '\"Juzgo con frecuencia las ideas de los demás por su valor práctico.\"', 1),
(39, '\"Me agobio si me obligan a acelerar mucho en el trabajo para cumplir un plazo.\"', 1),
(40, '\"En las reuniones, apoyo las ideas prácticas y realistas.\"', 1),
(41, '\"Es mejor gozar del momento presente que deleitarse pensando en el pasado o en el futuro.\"', 0),
(42, '\"Me molestan las personas que siempre desean apresurar las cosas.\"', 1),
(43, '\"Aporto idead nuevas y espontáneas en los grupos de discusión.\"', 1),
(44, '\"Pienso que son más consientes las decisiones fundamentadas en un minucioso análisis que las basadas en la institución.\"', 1),
(45, '\"Detecto frecuentemente la inconsistencia y puntos débiles en las argumentaciones de los demás.\"', 1),
(46, '\"Creo que es preciso saltarse las normas muchas más veces que cumplirlas.\"', 1),
(47, '\"A menudo caigo en la cuenta de otras formas mejores y más prácticas de hacer las cosas.\"', 1),
(48, '\"En conjunto hablo más de lo que escucho.\"', 1),
(49, '\"Prefiero distanciarme de los hechos y obsérvalos desde otras perspectivas.\"', 1),
(50, '\"Estoy convencido(a) que debe imponerse la lógica y el razonamiento.\"', 1),
(51, '\"Me gusta buscar nuevas experiencias.\"', 1),
(52, '\"Me gusta experimentar y aplicar cosas.\"', 1),
(53, '\"Pienso que debemos llegar pronto al grano, al meollo de los temas.\"', 1),
(54, '\"Siempre trato de conseguir conclusiones e ideas claras.\"', 1),
(55, '\"Prefiero discutir cuestiones concretas y no perder el tiempo con charlas vacías.\"', 1),
(56, '\"Me impaciento cuando me dan explicaciones irrelevantes e incoherentes.\"', 1),
(57, '\"Compruebo antes si las cosas funcionan realmente.\"', 1),
(58, '\"Hago varios borradores antes de la redacción definitiva de un trabajo.\"', 1),
(59, '\"Soy consiente de que en las discusiones ayudo a mantener a los demás centrados en el tema, evitando divagaciones.\"', 1),
(60, '\"Observo que, con frecuencia, soy uno(a) de los (as) más objetivos(as) y desapasionados(as) en las discusiones.\"', 1),
(61, '\"Cuando algo va mal, le quito importancia y trato de hacerlo mejor.\"', 1),
(62, '\"Rechazo ideas originales y espontáneas si no las veo prácticas.\"', 1),
(63, '\"Me gusta sopesar diversas alternativas antes de tomar una decisión.\"', 1),
(64, '\"Con frecuencia miro hacia adelante para prever el futuro.\"', 1),
(65, '\"En los debates y discusiones prefiero desempeñar un papel secundario antes que ser el(la) líder o el(la) que más participa.\"', 1),
(66, '\"Me molestan las personas que no actúan con lógica.\"', 1),
(67, '\"Me resulta incómodo tener que planificar y prever las cosas.\"', 1),
(68, '\"Creo que el fin justifica los medios en muchos casos.\"', 1),
(69, '\"Suelo reflexionar sobre los asuntos y problemas.\"', 1),
(70, '\"El trabajar a conciencia me llena de satisfacción y orgullo.\"', 1),
(71, '\"Ante los acontecimientos trato de descubrir los principios y teorías en que se basan.\"', 1),
(72, '\"Con tal de conseguir el objetivo que pretendo, soy capaz de herir los sentimientos ajenos.\"', 1),
(73, '\"No me importa hacer todo lo necesario para que sea efectivo mi trabajo.\"', 1),
(74, '\"Con frecuencia soy una de las personas que más anima las fiestas.\"', 1),
(75, '\"Me aburro enseguida en el trabajo metódico y minucioso.\"', 1),
(76, '\"La gente con frecuencia cree que soy poco sensible a sus sentimientos.\"', 1),
(77, '\"Suelo dejarme llevar por mis intuiciones.\"', 1),
(78, '\"Si trabajo en grupo procuro que soga un método y un orden.\"', 1),
(79, '\"Con frecuencia me interesa averiguar lo que piensa la gente.\"', 1),
(80, '\"Esquivo los temas subjetivos, ambiguos y poco claros.\"', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `preguntas`
--
ALTER TABLE `preguntas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `preguntas`
--
ALTER TABLE `preguntas`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
