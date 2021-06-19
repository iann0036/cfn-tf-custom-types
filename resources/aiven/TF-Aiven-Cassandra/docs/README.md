# TF::Aiven::Cassandra

CloudFormation equivalent of aiven_cassandra

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aiven::Cassandra",
    "Properties" : {
        "<a href="#cloudname" title="CloudName">CloudName</a>" : <i>String</i>,
        "<a href="#maintenancewindowdow" title="MaintenanceWindowDow">MaintenanceWindowDow</a>" : <i>String</i>,
        "<a href="#maintenancewindowtime" title="MaintenanceWindowTime">MaintenanceWindowTime</a>" : <i>String</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#projectvpcid" title="ProjectVpcId">ProjectVpcId</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>" : <i>Boolean</i>,
        "<a href="#cassandra" title="Cassandra">Cassandra</a>" : <i>[ <a href="cassandradefinition.md">CassandraDefinition</a>, ... ]</i>,
        "<a href="#cassandrauserconfig" title="CassandraUserConfig">CassandraUserConfig</a>" : <i>[ <a href="cassandrauserconfigdefinition.md">CassandraUserConfigDefinition</a>, ... ]</i>,
        "<a href="#serviceintegrations" title="ServiceIntegrations">ServiceIntegrations</a>" : <i>[ <a href="serviceintegrationsdefinition.md">ServiceIntegrationsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aiven::Cassandra
Properties:
    <a href="#cloudname" title="CloudName">CloudName</a>: <i>String</i>
    <a href="#maintenancewindowdow" title="MaintenanceWindowDow">MaintenanceWindowDow</a>: <i>String</i>
    <a href="#maintenancewindowtime" title="MaintenanceWindowTime">MaintenanceWindowTime</a>: <i>String</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#projectvpcid" title="ProjectVpcId">ProjectVpcId</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>: <i>Boolean</i>
    <a href="#cassandra" title="Cassandra">Cassandra</a>: <i>
      - <a href="cassandradefinition.md">CassandraDefinition</a></i>
    <a href="#cassandrauserconfig" title="CassandraUserConfig">CassandraUserConfig</a>: <i>
      - <a href="cassandrauserconfigdefinition.md">CassandraUserConfigDefinition</a></i>
    <a href="#serviceintegrations" title="ServiceIntegrations">ServiceIntegrations</a>: <i>
      - <a href="serviceintegrationsdefinition.md">ServiceIntegrationsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CloudName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowDow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cassandra

_Required_: No

_Type_: List of <a href="cassandradefinition.md">CassandraDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CassandraUserConfig

_Required_: No

_Type_: List of <a href="cassandrauserconfigdefinition.md">CassandraUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceIntegrations

_Required_: No

_Type_: List of <a href="serviceintegrationsdefinition.md">ServiceIntegrationsDefinition</a>

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

#### Components

Returns the <code>Components</code> value.

#### Id

Returns the <code>Id</code> value.

#### ServiceHost

Returns the <code>ServiceHost</code> value.

#### ServicePassword

Returns the <code>ServicePassword</code> value.

#### ServicePort

Returns the <code>ServicePort</code> value.

#### ServiceType

Returns the <code>ServiceType</code> value.

#### ServiceUri

Returns the <code>ServiceUri</code> value.

#### ServiceUsername

Returns the <code>ServiceUsername</code> value.

#### State

Returns the <code>State</code> value.

