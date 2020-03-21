# Terraform::OCI::DatabaseVmClusterNetwork Scans

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#ips" title="Ips">Ips</a>" : <i>[ String, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#ips" title="Ips">Ips</a>: <i>
      - String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
</pre>

## Properties

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ips

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

