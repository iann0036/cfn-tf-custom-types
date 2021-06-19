# TF::OCI::DataSafeTargetDatabase DatabaseDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>" : <i>String</i>,
    "<a href="#databasetype" title="DatabaseType">DatabaseType</a>" : <i>String</i>,
    "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
    "<a href="#infrastructuretype" title="InfrastructureType">InfrastructureType</a>" : <i>String</i>,
    "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
    "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#listenerport" title="ListenerPort">ListenerPort</a>" : <i>Double</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#vmclusterid" title="VmClusterId">VmClusterId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>: <i>String</i>
<a href="#databasetype" title="DatabaseType">DatabaseType</a>: <i>String</i>
<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
<a href="#infrastructuretype" title="InfrastructureType">InfrastructureType</a>: <i>String</i>
<a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
<a href="#listenerport" title="ListenerPort">ListenerPort</a>: <i>Double</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#vmclusterid" title="VmClusterId">VmClusterId</a>: <i>String</i>
</pre>

## Properties

#### AutonomousDatabaseId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSystemId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfrastructureType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

