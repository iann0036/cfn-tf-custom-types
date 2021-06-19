# TF::AzureRM::NetappVolume DataProtectionReplicationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
    "<a href="#remotevolumelocation" title="RemoteVolumeLocation">RemoteVolumeLocation</a>" : <i>String</i>,
    "<a href="#remotevolumeresourceid" title="RemoteVolumeResourceId">RemoteVolumeResourceId</a>" : <i>String</i>,
    "<a href="#replicationfrequency" title="ReplicationFrequency">ReplicationFrequency</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
<a href="#remotevolumelocation" title="RemoteVolumeLocation">RemoteVolumeLocation</a>: <i>String</i>
<a href="#remotevolumeresourceid" title="RemoteVolumeResourceId">RemoteVolumeResourceId</a>: <i>String</i>
<a href="#replicationfrequency" title="ReplicationFrequency">ReplicationFrequency</a>: <i>String</i>
</pre>

## Properties

#### EndpointType

The endpoint type, default value is `dst` for destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteVolumeLocation

Location of the primary volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteVolumeResourceId

Resource ID of the primary volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationFrequency

Replication frequency, supported values are '10minutes', 'hourly', 'daily', values are case sensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

