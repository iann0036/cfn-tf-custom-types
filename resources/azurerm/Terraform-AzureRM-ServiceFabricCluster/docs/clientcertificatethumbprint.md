# Terraform::AzureRM::ServiceFabricCluster ClientCertificateThumbprint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isadmin" title="IsAdmin">IsAdmin</a>" : <i>Boolean</i>,
    "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#isadmin" title="IsAdmin">IsAdmin</a>: <i>Boolean</i>
<a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
</pre>

## Properties

#### IsAdmin

Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbprint

The Thumbprint associated with the Client Certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

