# Terraform::OPC::LbaasPolicy ResourceAccessControlPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deniedclients" title="DeniedClients">DeniedClients</a>" : <i>[ String, ... ]</i>,
    "<a href="#disposition" title="Disposition">Disposition</a>" : <i>String</i>,
    "<a href="#permittedclients" title="PermittedClients">PermittedClients</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#deniedclients" title="DeniedClients">DeniedClients</a>: <i>
      - String</i>
<a href="#disposition" title="Disposition">Disposition</a>: <i>String</i>
<a href="#permittedclients" title="PermittedClients">PermittedClients</a>: <i>
      - String</i>
</pre>

## Properties

#### DeniedClients

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disposition

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedClients

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

