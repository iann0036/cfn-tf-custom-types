# Terraform::OCI::DnsZone ExternalMasters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#tsigkeyid" title="TsigKeyId">TsigKeyId</a>" : <i>String</i>,
    "<a href="#tsig" title="Tsig">Tsig</a>" : <i>[ <a href="externalmasters-tsig.md">Tsig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#tsigkeyid" title="TsigKeyId">TsigKeyId</a>: <i>String</i>
<a href="#tsig" title="Tsig">Tsig</a>: <i>
      - <a href="externalmasters-tsig.md">Tsig</a></i>
</pre>

## Properties

#### Address

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TsigKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tsig

_Required_: No

_Type_: List of <a href="externalmasters-tsig.md">Tsig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

