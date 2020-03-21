# Terraform::AWS::DirectoryServiceDirectory ConnectSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customerdnsips" title="CustomerDnsIps">CustomerDnsIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#customerusername" title="CustomerUsername">CustomerUsername</a>" : <i>String</i>,
    "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#customerdnsips" title="CustomerDnsIps">CustomerDnsIps</a>: <i>
      - String</i>
<a href="#customerusername" title="CustomerUsername">CustomerUsername</a>: <i>String</i>
<a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### CustomerDnsIps

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerUsername

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

