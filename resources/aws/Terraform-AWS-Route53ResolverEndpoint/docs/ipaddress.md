# Terraform::AWS::Route53ResolverEndpoint IpAddress

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### Ip

The IP address in the subnet that you want to use for DNS queries.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the subnet that contains the IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

