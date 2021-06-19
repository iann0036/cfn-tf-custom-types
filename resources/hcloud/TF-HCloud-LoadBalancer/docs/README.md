# TF::HCloud::LoadBalancer

Provides a Hetzner Cloud Load Balancer to represent a Load Balancer in the Hetzner Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::LoadBalancer",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkzone" title="NetworkZone">NetworkZone</a>" : <i>String</i>,
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>[ <a href="algorithmdefinition.md">AlgorithmDefinition</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::LoadBalancer
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkzone" title="NetworkZone">NetworkZone</a>: <i>String</i>
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>
      - <a href="algorithmdefinition.md">AlgorithmDefinition</a></i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
</pre>

## Properties

#### Labels

User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerType

Type of the Load Balancer.
- `location` - (Optional, string) Location of the Load Balancer. Require when no network_zone is set.
- `network_zone` - (Optional, string) Network Zone of the Load Balancer. Require when no location is set.
- `algorithm` - (Optional) Configuration of the algorithm the Load Balancer use.
- `target` - (Optional, list) List of targets of the Load Balancer.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Location of the Load Balancer. Require when no network_zone is set.
- `network_zone` - (Optional, string) Network Zone of the Load Balancer. Require when no location is set.
- `algorithm` - (Optional) Configuration of the algorithm the Load Balancer use.
- `target` - (Optional, list) List of targets of the Load Balancer.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Load Balancer.
- `load_balancer_type` - (Required, string) Type of the Load Balancer.
- `location` - (Optional, string) Location of the Load Balancer. Require when no network_zone is set.
- `network_zone` - (Optional, string) Network Zone of the Load Balancer. Require when no location is set.
- `algorithm` - (Optional) Configuration of the algorithm the Load Balancer use.
- `target` - (Optional, list) List of targets of the Load Balancer.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkZone

Network Zone of the Load Balancer. Require when no location is set.
- `algorithm` - (Optional) Configuration of the algorithm the Load Balancer use.
- `target` - (Optional, list) List of targets of the Load Balancer.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

_Required_: No

_Type_: List of <a href="algorithmdefinition.md">AlgorithmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Ipv4

Returns the <code>Ipv4</code> value.

#### Ipv6

Returns the <code>Ipv6</code> value.

#### NetworkId

Returns the <code>NetworkId</code> value.

#### NetworkIp

Returns the <code>NetworkIp</code> value.

