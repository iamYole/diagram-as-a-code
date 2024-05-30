from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, Route53, InternetGateway
from diagrams.aws.database import RDS
from diagrams.onprem.client import Users

with Diagram(name="AWS Multiple Website Project", filename="Diagrams/image", show=True, direction="TB"):
    dns = Route53("dns")
    lb = ELB('lb')
    ig = InternetGateway("Internet Gateway")
    
    users = Users("")
    users - Users("")

    with Cluster("services"):
        svc_group = [EC2("web1"),
                       EC2("web2"),
                       EC2("web3")]
        

users >> dns >> ig