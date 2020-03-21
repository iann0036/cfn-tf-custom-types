# Terraform::Google::ContainerCluster AuthenticatorGroupsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
</pre>

## Properties

#### SecurityGroup

The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format `gke-security-groups@yourdomain.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

