# Terraform::Consul::AclRole ServiceIdentities

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datacenters" title="Datacenters">Datacenters</a>" : <i>[ String, ... ]</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#datacenters" title="Datacenters">Datacenters</a>: <i>
      - String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### Datacenters

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

