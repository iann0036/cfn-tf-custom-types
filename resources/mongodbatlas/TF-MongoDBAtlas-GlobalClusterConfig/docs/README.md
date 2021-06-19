# TF::MongoDBAtlas::GlobalClusterConfig

`mongodbatlas_global_cluster_config` provides a Global Cluster Configuration resource.


-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::GlobalClusterConfig",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#customzonemappings" title="CustomZoneMappings">CustomZoneMappings</a>" : <i>[ <a href="customzonemappingsdefinition.md">CustomZoneMappingsDefinition</a>, ... ]</i>,
        "<a href="#managednamespaces" title="ManagedNamespaces">ManagedNamespaces</a>" : <i>[ <a href="managednamespacesdefinition.md">ManagedNamespacesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::GlobalClusterConfig
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#customzonemappings" title="CustomZoneMappings">CustomZoneMappings</a>: <i>
      - <a href="customzonemappingsdefinition.md">CustomZoneMappingsDefinition</a></i>
    <a href="#managednamespaces" title="ManagedNamespaces">ManagedNamespaces</a>: <i>
      - <a href="managednamespacesdefinition.md">ManagedNamespacesDefinition</a></i>
</pre>

## Properties

#### ClusterName

The name of the Global Cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to create the database user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomZoneMappings

_Required_: No

_Type_: List of <a href="customzonemappingsdefinition.md">CustomZoneMappingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedNamespaces

_Required_: No

_Type_: List of <a href="managednamespacesdefinition.md">ManagedNamespacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CustomZoneMapping

Returns the <code>CustomZoneMapping</code> value.

#### Id

Returns the <code>Id</code> value.

