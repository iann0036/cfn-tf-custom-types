# Terraform::Kubernetes::Daemonset Spec HostAliases

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostnames" title="Hostnames">Hostnames</a>" : <i>[ String, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostnames" title="Hostnames">Hostnames</a>: <i>
      - String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
</pre>

## Properties

#### Hostnames

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

