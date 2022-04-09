import React, { Component, ReactNode } from "react";
import Container from "react-bootstrap/esm/Container";
import Navbar from "react-bootstrap/esm/Navbar";
import Nav from "react-bootstrap/esm/Nav";
import logo from '../../../assets/logo.png';
import styles from './Toolbar.module.css';

interface ToolbarStates 
{
  activeItem?: boolean;
}

interface ToolbarProps
{
  margin?: number;
  activeItem?: boolean;
}

class Toolbar extends Component<ToolbarProps, ToolbarStates>
{
  constructor(props: ToolbarProps)
  {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  render(): ReactNode {
    return (
      <> 
        <Navbar className={styles.navbar} style={{ marginBottom: this.props.margin }} variant="dark">
          <Container>
            <Navbar.Brand href="/">
              <img
                alt=""
                src={logo}
                width="32"
                height="32"
                className="d-inline-block align-top"
              />{' '}
              <p className={styles.title}>
                Quantex
              </p>
            </Navbar.Brand>
            <Nav>
              <Nav.Link className={styles.element} href="/">Home</Nav.Link>
              <Nav.Link className={styles.element} href="/instruments">Instruments</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
      </>
    )
  }
}

export default Toolbar;
