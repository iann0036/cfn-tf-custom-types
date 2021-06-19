# TF::OVH::CloudProjectKubeNodepool

Creates a nodepool in a kubernetes managed cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::CloudProjectKubeNodepool",
    "Properties" : {
        "<a href="#antiaffinity" title="AntiAffinity">AntiAffinity</a>" : <i>Boolean</i>,
        "<a href="#autoscale" title="Autoscale">Autoscale</a>" : <i>Boolean</i>,
        "<a href="#desirednodes" title="DesiredNodes">DesiredNodes</a>" : <i>Double</i>,
        "<a href="#flavorname" title="FlavorName">FlavorName</a>" : <i>String</i>,
        "<a href="#kubeid" title="KubeId">KubeId</a>" : <i>String</i>,
        "<a href="#maxnodes" title="MaxNodes">MaxNodes</a>" : <i>Double</i>,
        "<a href="#minnodes" title="MinNodes">MinNodes</a>" : <i>Double</i>,
        "<a href="#monthlybilled" title="MonthlyBilled">MonthlyBilled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::CloudProjectKubeNodepool
Properties:
    <a href="#antiaffinity" title="AntiAffinity">AntiAffinity</a>: <i>Boolean</i>
    <a href="#autoscale" title="Autoscale">Autoscale</a>: <i>Boolean</i>
    <a href="#desirednodes" title="DesiredNodes">DesiredNodes</a>: <i>Double</i>
    <a href="#flavorname" title="FlavorName">FlavorName</a>: <i>String</i>
    <a href="#kubeid" title="KubeId">KubeId</a>: <i>String</i>
    <a href="#maxnodes" title="MaxNodes">MaxNodes</a>: <i>Double</i>
    <a href="#minnodes" title="MinNodes">MinNodes</a>: <i>Double</i>
    <a href="#monthlybilled" title="MonthlyBilled">MonthlyBilled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### AntiAffinity

should the pool use the anti-affinity feature. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscale

Enable auto-scaling for the pool. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredNodes

number of nodes to start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorName

a valid OVH public cloud flavor ID in which the nodes will be start.
cluster will be available. Ex.: "b2-7". Changing this value recreates the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeId

The id of the managed kubernetes cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNodes

maximum number of nodes allowed in the pool.
Setting `desired_nodes` over this value will raise an error.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNodes

minimum number of nodes allowed in the pool.
Setting `desired_nodes` under this value will raise an error.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlyBilled

should the nodes be billed on a monthly basis. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the nodepool.
Changing this value recreates the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The id of the public cloud project. If omitted,
the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailableNodes

Returns the <code>AvailableNodes</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### CurrentNodes

Returns the <code>CurrentNodes</code> value.

#### Flavor

Returns the <code>Flavor</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProjectId

Returns the <code>ProjectId</code> value.

#### SizeStatus

Returns the <code>SizeStatus</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpToDateNodes

Returns the <code>UpToDateNodes</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

