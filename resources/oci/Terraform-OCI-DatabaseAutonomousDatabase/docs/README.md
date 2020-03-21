# Terraform::OCI::DatabaseAutonomousDatabase

CloudFormation equivalent of oci_database_autonomous_database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseAutonomousDatabase",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>" : <i>String</i>,
        "<a href="#autonomousdatabasebackupid" title="AutonomousDatabaseBackupId">AutonomousDatabaseBackupId</a>" : <i>String</i>,
        "<a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>" : <i>String</i>,
        "<a href="#clonetype" title="CloneType">CloneType</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#connectionstrings" title="ConnectionStrings">ConnectionStrings</a>" : <i>[ &lt;a href=&#34;connectionstrings.md&#34;&gt;ConnectionStrings&lt;/a&gt;, ... ]</i>,
        "<a href="#connectionurls" title="ConnectionUrls">ConnectionUrls</a>" : <i>[ &lt;a href=&#34;connectionurls.md&#34;&gt;ConnectionUrls&lt;/a&gt;, ... ]</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#datasafestatus" title="DataSafeStatus">DataSafeStatus</a>" : <i>String</i>,
        "<a href="#datastoragesizeintbs" title="DataStorageSizeInTbs">DataStorageSizeInTbs</a>" : <i>Double</i>,
        "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#dbworkload" title="DbWorkload">DbWorkload</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>" : <i>Boolean</i>,
        "<a href="#isdedicated" title="IsDedicated">IsDedicated</a>" : <i>Boolean</i>,
        "<a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>" : <i>Boolean</i>,
        "<a href="#ispreview" title="IsPreview">IsPreview</a>" : <i>Boolean</i>,
        "<a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>" : <i>Boolean</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>" : <i>String</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#privateendpoint" title="PrivateEndpoint">PrivateEndpoint</a>" : <i>String</i>,
        "<a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>" : <i>String</i>,
        "<a href="#serviceconsoleurl" title="ServiceConsoleUrl">ServiceConsoleUrl</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceid" title="SourceId">SourceId</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#systemtags" title="SystemTags">SystemTags</a>" : <i>[ &lt;a href=&#34;systemtags.md&#34;&gt;SystemTags&lt;/a&gt;, ... ]</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#timedeletionoffreeautonomousdatabase" title="TimeDeletionOfFreeAutonomousDatabase">TimeDeletionOfFreeAutonomousDatabase</a>" : <i>String</i>,
        "<a href="#timemaintenancebegin" title="TimeMaintenanceBegin">TimeMaintenanceBegin</a>" : <i>String</i>,
        "<a href="#timemaintenanceend" title="TimeMaintenanceEnd">TimeMaintenanceEnd</a>" : <i>String</i>,
        "<a href="#timereclamationoffreeautonomousdatabase" title="TimeReclamationOfFreeAutonomousDatabase">TimeReclamationOfFreeAutonomousDatabase</a>" : <i>String</i>,
        "<a href="#timestamp" title="Timestamp">Timestamp</a>" : <i>String</i>,
        "<a href="#useddatastoragesizeintbs" title="UsedDataStorageSizeInTbs">UsedDataStorageSizeInTbs</a>" : <i>Double</i>,
        "<a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseAutonomousDatabase
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>: <i>String</i>
    <a href="#autonomousdatabasebackupid" title="AutonomousDatabaseBackupId">AutonomousDatabaseBackupId</a>: <i>String</i>
    <a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>: <i>String</i>
    <a href="#clonetype" title="CloneType">CloneType</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#connectionstrings" title="ConnectionStrings">ConnectionStrings</a>: <i>
      - &lt;a href=&#34;connectionstrings.md&#34;&gt;ConnectionStrings&lt;/a&gt;</i>
    <a href="#connectionurls" title="ConnectionUrls">ConnectionUrls</a>: <i>
      - &lt;a href=&#34;connectionurls.md&#34;&gt;ConnectionUrls&lt;/a&gt;</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#datasafestatus" title="DataSafeStatus">DataSafeStatus</a>: <i>String</i>
    <a href="#datastoragesizeintbs" title="DataStorageSizeInTbs">DataStorageSizeInTbs</a>: <i>Double</i>
    <a href="#dbname" title="DbName">DbName</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#dbworkload" title="DbWorkload">DbWorkload</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>: <i>Boolean</i>
    <a href="#isdedicated" title="IsDedicated">IsDedicated</a>: <i>Boolean</i>
    <a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>: <i>Boolean</i>
    <a href="#ispreview" title="IsPreview">IsPreview</a>: <i>Boolean</i>
    <a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>: <i>Boolean</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>: <i>String</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#privateendpoint" title="PrivateEndpoint">PrivateEndpoint</a>: <i>String</i>
    <a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>: <i>String</i>
    <a href="#serviceconsoleurl" title="ServiceConsoleUrl">ServiceConsoleUrl</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceid" title="SourceId">SourceId</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#systemtags" title="SystemTags">SystemTags</a>: <i>
      - &lt;a href=&#34;systemtags.md&#34;&gt;SystemTags&lt;/a&gt;</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#timedeletionoffreeautonomousdatabase" title="TimeDeletionOfFreeAutonomousDatabase">TimeDeletionOfFreeAutonomousDatabase</a>: <i>String</i>
    <a href="#timemaintenancebegin" title="TimeMaintenanceBegin">TimeMaintenanceBegin</a>: <i>String</i>
    <a href="#timemaintenanceend" title="TimeMaintenanceEnd">TimeMaintenanceEnd</a>: <i>String</i>
    <a href="#timereclamationoffreeautonomousdatabase" title="TimeReclamationOfFreeAutonomousDatabase">TimeReclamationOfFreeAutonomousDatabase</a>: <i>String</i>
    <a href="#timestamp" title="Timestamp">Timestamp</a>: <i>String</i>
    <a href="#useddatastoragesizeintbs" title="UsedDataStorageSizeInTbs">UsedDataStorageSizeInTbs</a>: <i>Double</i>
    <a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousContainerDatabaseId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousDatabaseBackupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousDatabaseId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloneType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionStrings

_Required_: No

_Type_: List of &lt;a href=&#34;connectionstrings.md&#34;&gt;ConnectionStrings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionUrls

_Required_: No

_Type_: List of &lt;a href=&#34;connectionurls.md&#34;&gt;ConnectionUrls&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSafeStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInTbs

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoScalingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDedicated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFreeTier

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPreview

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPreviewVersionWithServiceTermsAccepted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleDetails

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpointLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConsoleUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemTags

_Required_: No

_Type_: List of &lt;a href=&#34;systemtags.md&#34;&gt;SystemTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeDeletionOfFreeAutonomousDatabase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeMaintenanceBegin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeMaintenanceEnd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeReclamationOfFreeAutonomousDatabase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsedDataStorageSizeInTbs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhitelistedIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionStrings

Returns the &lt;code&gt;ConnectionStrings&lt;/code&gt; value.

#### ConnectionUrls

Returns the &lt;code&gt;ConnectionUrls&lt;/code&gt; value.

#### IsPreview

Returns the &lt;code&gt;IsPreview&lt;/code&gt; value.

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### PrivateEndpoint

Returns the &lt;code&gt;PrivateEndpoint&lt;/code&gt; value.

#### ServiceConsoleUrl

Returns the &lt;code&gt;ServiceConsoleUrl&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### SystemTags

Returns the &lt;code&gt;SystemTags&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

#### TimeDeletionOfFreeAutonomousDatabase

Returns the &lt;code&gt;TimeDeletionOfFreeAutonomousDatabase&lt;/code&gt; value.

#### TimeMaintenanceBegin

Returns the &lt;code&gt;TimeMaintenanceBegin&lt;/code&gt; value.

#### TimeMaintenanceEnd

Returns the &lt;code&gt;TimeMaintenanceEnd&lt;/code&gt; value.

#### TimeReclamationOfFreeAutonomousDatabase

Returns the &lt;code&gt;TimeReclamationOfFreeAutonomousDatabase&lt;/code&gt; value.

#### UsedDataStorageSizeInTbs

Returns the &lt;code&gt;UsedDataStorageSizeInTbs&lt;/code&gt; value.

