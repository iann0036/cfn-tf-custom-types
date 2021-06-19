# TF::AVI::Siteversion

The SiteVersion resource allows the creation and management of Avi SiteVersion

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Siteversion",
    "Properties" : {
        "<a href="#datetime" title="Datetime">Datetime</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#prevtargetversion" title="PrevTargetVersion">PrevTargetVersion</a>" : <i>Double</i>,
        "<a href="#replicationstate" title="ReplicationState">ReplicationState</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#targettimeline" title="TargetTimeline">TargetTimeline</a>" : <i>String</i>,
        "<a href="#targetversion" title="TargetVersion">TargetVersion</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#timeline" title="Timeline">Timeline</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#versiontype" title="VersionType">VersionType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Siteversion
Properties:
    <a href="#datetime" title="Datetime">Datetime</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#prevtargetversion" title="PrevTargetVersion">PrevTargetVersion</a>: <i>Double</i>
    <a href="#replicationstate" title="ReplicationState">ReplicationState</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#targettimeline" title="TargetTimeline">TargetTimeline</a>: <i>String</i>
    <a href="#targetversion" title="TargetVersion">TargetVersion</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#timeline" title="Timeline">Timeline</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#versiontype" title="VersionType">VersionType</a>: <i>String</i>
</pre>

## Properties

#### Datetime

This field represents the creation time of the federateddiff. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the site. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrevTargetVersion

Previous targer version for a site. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationState

Replication state for a site. Enum options - REPLICATION_STATE_FASTFORWARD, REPLICATION_STATE_FORCESYNC, REPLICATION_STATE_STREAMING, REPLICATION_STATE_SUSPENDED, REPLICATION_STATE_INIT, REPLICATION_STATE_WAIT, REPLICATION_STATE_NOT_APPLICABLE. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

Cluster uuid of the site. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTimeline

Target timeline of the site. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetVersion

Target version of the site. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant that this object belongs to. It is a reference to an object of type tenant. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeline

Timeline of the site. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Version of the site. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionType

Type of message for which version is maintained. Enum options - CONFIG_VERSION, HEALTH_STATUS_VERSION. Field introduced in 20.1.1.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

