# TF::Metal::Project BgpConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
    "<a href="#md5" title="Md5">Md5</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
<a href="#md5" title="Md5">Md5</a>: <i>String</i>
</pre>

## Properties

#### Asn

Autonomous System Number for local BGP deployment.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentType

`private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Equinix Metal engineers.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Md5

Password for BGP session in plaintext (not a checksum).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

