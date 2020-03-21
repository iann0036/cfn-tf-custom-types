# Terraform::OraclePaaS::JavaServiceInstance WeblogicServer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backupvolumesize" title="BackupVolumeSize">BackupVolumeSize</a>" : <i>String</i>,
    "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
    "<a href="#connectstring" title="ConnectString">ConnectString</a>" : <i>String</i>,
    "<a href="#ipreservations" title="IpReservations">IpReservations</a>" : <i>[ String, ... ]</i>,
    "<a href="#middlewarevolumesize" title="MiddlewareVolumeSize">MiddlewareVolumeSize</a>" : <i>String</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#upperstackproductname" title="UpperStackProductName">UpperStackProductName</a>" : <i>String</i>,
    "<a href="#admin" title="Admin">Admin</a>" : <i>[ &lt;a href=&#34;weblogicserver-admin.md&#34;&gt;Admin&lt;/a&gt;, ... ]</i>,
    "<a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>" : <i>[ &lt;a href=&#34;weblogicserver-applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;, ... ]</i>,
    "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ &lt;a href=&#34;weblogicserver-cluster.md&#34;&gt;Cluster&lt;/a&gt;, ... ]</i>,
    "<a href="#database" title="Database">Database</a>" : <i>[ &lt;a href=&#34;weblogicserver-database.md&#34;&gt;Database&lt;/a&gt;, ... ]</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>[ &lt;a href=&#34;weblogicserver-domain.md&#34;&gt;Domain&lt;/a&gt;, ... ]</i>,
    "<a href="#managedservers" title="ManagedServers">ManagedServers</a>" : <i>[ &lt;a href=&#34;weblogicserver-managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;, ... ]</i>,
    "<a href="#nodemanager" title="NodeManager">NodeManager</a>" : <i>[ &lt;a href=&#34;weblogicserver-nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;weblogicserver-ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backupvolumesize" title="BackupVolumeSize">BackupVolumeSize</a>: <i>String</i>
<a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
<a href="#connectstring" title="ConnectString">ConnectString</a>: <i>String</i>
<a href="#ipreservations" title="IpReservations">IpReservations</a>: <i>
      - String</i>
<a href="#middlewarevolumesize" title="MiddlewareVolumeSize">MiddlewareVolumeSize</a>: <i>String</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#upperstackproductname" title="UpperStackProductName">UpperStackProductName</a>: <i>String</i>
<a href="#admin" title="Admin">Admin</a>: <i>
      - &lt;a href=&#34;weblogicserver-admin.md&#34;&gt;Admin&lt;/a&gt;</i>
<a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>: <i>
      - &lt;a href=&#34;weblogicserver-applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;</i>
<a href="#cluster" title="Cluster">Cluster</a>: <i>
      - &lt;a href=&#34;weblogicserver-cluster.md&#34;&gt;Cluster&lt;/a&gt;</i>
<a href="#database" title="Database">Database</a>: <i>
      - &lt;a href=&#34;weblogicserver-database.md&#34;&gt;Database&lt;/a&gt;</i>
<a href="#domain" title="Domain">Domain</a>: <i>
      - &lt;a href=&#34;weblogicserver-domain.md&#34;&gt;Domain&lt;/a&gt;</i>
<a href="#managedservers" title="ManagedServers">ManagedServers</a>: <i>
      - &lt;a href=&#34;weblogicserver-managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;</i>
<a href="#nodemanager" title="NodeManager">NodeManager</a>: <i>
      - &lt;a href=&#34;weblogicserver-nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;weblogicserver-ports.md&#34;&gt;Ports&lt;/a&gt;</i>
</pre>

## Properties

#### BackupVolumeSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectString

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReservations

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddlewareVolumeSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpperStackProductName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-admin.md&#34;&gt;Admin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationDatabase

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-cluster.md&#34;&gt;Cluster&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-database.md&#34;&gt;Database&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-domain.md&#34;&gt;Domain&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServers

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeManager

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No
_Type_: List of &lt;a href=&#34;weblogicserver-ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

