# TF::Databricks::MwsLogDelivery

CloudFormation equivalent of databricks_mws_log_delivery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::MwsLogDelivery",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>String</i>,
        "<a href="#configname" title="ConfigName">ConfigName</a>" : <i>String</i>,
        "<a href="#credentialsid" title="CredentialsId">CredentialsId</a>" : <i>String</i>,
        "<a href="#deliverypathprefix" title="DeliveryPathPrefix">DeliveryPathPrefix</a>" : <i>String</i>,
        "<a href="#deliverystarttime" title="DeliveryStartTime">DeliveryStartTime</a>" : <i>String</i>,
        "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>,
        "<a href="#outputformat" title="OutputFormat">OutputFormat</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#storageconfigurationid" title="StorageConfigurationId">StorageConfigurationId</a>" : <i>String</i>,
        "<a href="#workspaceidsfilter" title="WorkspaceIdsFilter">WorkspaceIdsFilter</a>" : <i>[ Double, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::MwsLogDelivery
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>String</i>
    <a href="#configname" title="ConfigName">ConfigName</a>: <i>String</i>
    <a href="#credentialsid" title="CredentialsId">CredentialsId</a>: <i>String</i>
    <a href="#deliverypathprefix" title="DeliveryPathPrefix">DeliveryPathPrefix</a>: <i>String</i>
    <a href="#deliverystarttime" title="DeliveryStartTime">DeliveryStartTime</a>: <i>String</i>
    <a href="#logtype" title="LogType">LogType</a>: <i>String</i>
    <a href="#outputformat" title="OutputFormat">OutputFormat</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#storageconfigurationid" title="StorageConfigurationId">StorageConfigurationId</a>: <i>String</i>
    <a href="#workspaceidsfilter" title="WorkspaceIdsFilter">WorkspaceIdsFilter</a>: <i>
      - Double</i>
</pre>

## Properties

#### AccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryPathPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryStartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormat

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConfigurationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceIdsFilter

_Required_: No

_Type_: List of Double

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

