import React, { useEffect, useState } from 'react';
import { Card, Table, Button, Modal, Form } from 'react-bootstrap';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedActivity, setSelectedActivity] = useState(null);
  const [editName, setEditName] = useState("");

  useEffect(() => {
    fetch('https://symmetrical-guide-65v9g9p75pg2qxx-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  const handleShowModal = (activity) => {
    setSelectedActivity(activity);
    setEditName(activity.name);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedActivity(null);
  };

  return (
    <div className="container mt-4">
      <Card>
        <Card.Body>
          <Card.Title as="h2" className="mb-4 text-primary">Activities</Card.Title>
          <Button variant="success" className="mb-3" onClick={() => alert('Add Activity form coming soon!')}>
            + Add Activity
          </Button>
          <Table striped bordered hover responsive>
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(activity => (
                <tr key={activity.id}>
                  <td>
                    <a href="#" className="link-primary" onClick={() => handleShowModal(activity)}>
                      {activity.name}
                    </a>
                  </td>
                  <td>
                    <Button variant="primary" size="sm" onClick={() => handleShowModal(activity)}>
                      View
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card.Body>
      </Card>
      {/* Modal */}
      <Modal show={showModal} onHide={handleCloseModal} centered>
        <Modal.Header closeButton className="bg-primary text-white">
          <Modal.Title>Activity Details</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {selectedActivity && (
            <>
              <p><strong>Name:</strong> {selectedActivity.name}</p>
              {/* Example form for editing (not functional) */}
              <Form>
                <Form.Group className="mb-3" controlId="editName">
                  <Form.Label>Edit Name</Form.Label>
                  <Form.Control
                    type="text"
                    value={editName}
                    onChange={e => setEditName(e.target.value)}
                  />
                </Form.Group>
                <Button variant="success" disabled>Save (Demo)</Button>
              </Form>
            </>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseModal}>Close</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default Activities;
