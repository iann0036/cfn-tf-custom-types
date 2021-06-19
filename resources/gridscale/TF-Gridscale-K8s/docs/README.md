# TF::Gridscale::K8s

Provides a k8s cluster resource. This can be used to create, modify, and delete k8s cluster resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::K8s",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#release" title="Release">Release</a>" : <i>String</i>,
        "<a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>" : <i>String</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ <a href="nodepooldefinition.md">NodePoolDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::K8s
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#release" title="Release">Release</a>: <i>String</i>
    <a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>: <i>String</i>
    <a href="#nodepool" title="NodePool">NodePool</a>: <i>
      - <a href="nodepooldefinition.md">NodePoolDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the node pool.
* `node_count` - Number of worker nodes.
* `cores` - (Immutable) Cores per worker node.
* `memory` - (Immutable) Memory per worker node (in GiB).
* `storage` - (Immutable) Storage per worker node (in GiB).
* `storage_type` - (Immutable) Storage type (one of storage, storage_high, storage_insane).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Release

The Kubernetes release of this instance. Define which release will be used to create the cluster. For convenience, please use [gscloud](https://github.com/gridscale/gscloud) to get the list of available release numbers.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityZoneUuid

Security zone UUID linked to the Kubernetes resource. If `security_zone_uuid` is not set, the default security zone will be created (if it doesn't exist) and linked. A change of this argument necessitates the re-creation of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: No

_Type_: List of <a href="nodepooldefinition.md">NodePoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kubeconfig

Returns the <code>Kubeconfig</code> value.

#### ListenPort

Returns the <code>ListenPort</code> value.

#### NetworkUuid

Returns the <code>NetworkUuid</code> value.

#### ServiceTemplateUuid

Returns the <code>ServiceTemplateUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutes

Returns the <code>UsageInMinutes</code> value.

