import React, { useEffect, useState } from 'react';
import { Card, Table, Button } from 'react-bootstrap';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedEntry, setSelectedEntry] = useState(null);

  useEffect(() => {
    fetch('https://symmetrical-guide-65v9g9p75pg2qxx-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  const handleShowModal = (entry) => {
    setSelectedEntry(entry);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedEntry(null);
  };

  return (
    <div className="container mt-4">
      <Card>
        <Card.Body>
          <Card.Title as="h2" className="mb-4">Leaderboard</Card.Title>
          <Table striped bordered hover responsive>
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Score</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map(entry => (
                <tr key={entry.id}>
                  <td>{entry.name}</td>
                  <td>{entry.score}</td>
                  <td>
                    <Button variant="primary" size="sm" onClick={() => handleShowModal(entry)}>
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
      {showModal && selectedEntry && (
        <div className="modal show d-block" tabIndex="-1" role="dialog" style={{ background: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Leaderboard Entry</h5>
                <Button variant="close" aria-label="Close" onClick={handleCloseModal}>
                  <span aria-hidden="true">&times;</span>
                </Button>
              </div>
              <div className="modal-body">
                <p><strong>Name:</strong> {selectedEntry.name}</p>
                <p><strong>Score:</strong> {selectedEntry.score}</p>
              </div>
              <div className="modal-footer">
                <Button variant="secondary" onClick={handleCloseModal}>Close</Button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
