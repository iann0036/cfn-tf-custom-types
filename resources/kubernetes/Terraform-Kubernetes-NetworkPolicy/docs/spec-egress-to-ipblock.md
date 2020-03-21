# Terraform::Kubernetes::NetworkPolicy Spec Egress To IpBlock

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
    "<a href="#except" title="Except">Except</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
<a href="#except" title="Except">Except</a>: <i>
      - String</i>
</pre>

## Properties

#### Cidr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Except

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

