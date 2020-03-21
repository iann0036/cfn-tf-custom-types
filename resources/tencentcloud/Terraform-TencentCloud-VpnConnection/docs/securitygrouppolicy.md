# Terraform::TencentCloud::VpnConnection SecurityGroupPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#localcidrblock" title="LocalCidrBlock">LocalCidrBlock</a>" : <i>String</i>,
    "<a href="#remotecidrblock" title="RemoteCidrBlock">RemoteCidrBlock</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#localcidrblock" title="LocalCidrBlock">LocalCidrBlock</a>: <i>String</i>
<a href="#remotecidrblock" title="RemoteCidrBlock">RemoteCidrBlock</a>: <i>
      - String</i>
</pre>

## Properties

#### LocalCidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteCidrBlock

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

