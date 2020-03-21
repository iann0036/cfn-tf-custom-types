# Terraform::FlexibleEngine::MlsInstanceV1 Network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availablezone" title="AvailableZone">AvailableZone</a>" : <i>String</i>,
    "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ <a href="network-publicip.md">PublicIp</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availablezone" title="AvailableZone">AvailableZone</a>: <i>String</i>
<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - <a href="network-publicip.md">PublicIp</a></i>
</pre>

## Properties

#### AvailableZone

Specifies the AZ of the instance.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

Specifies the ID of the security group of the instance.
Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Specifies the ID of the subnet where the instance resides.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Specifies the ID of the virtual private cloud (VPC) where the
instance resides. Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: List of <a href="network-publicip.md">PublicIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

