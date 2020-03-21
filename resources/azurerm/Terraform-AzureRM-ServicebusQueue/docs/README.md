# Terraform::AzureRM::ServicebusQueue

CloudFormation equivalent of azurerm_servicebus_queue

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ServicebusQueue",
    "Properties" : {
        "<a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>" : <i>String</i>,
        "<a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>" : <i>Boolean</i>,
        "<a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>" : <i>String</i>,
        "<a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>" : <i>String</i>,
        "<a href="#enableexpress" title="EnableExpress">EnableExpress</a>" : <i>Boolean</i>,
        "<a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#lockduration" title="LockDuration">LockDuration</a>" : <i>String</i>,
        "<a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>" : <i>Double</i>,
        "<a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
        "<a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>" : <i>Boolean</i>,
        "<a href="#requiressession" title="RequiresSession">RequiresSession</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ServicebusQueue
Properties:
    <a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>: <i>String</i>
    <a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>: <i>Boolean</i>
    <a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>: <i>String</i>
    <a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>: <i>String</i>
    <a href="#enableexpress" title="EnableExpress">EnableExpress</a>: <i>Boolean</i>
    <a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#lockduration" title="LockDuration">LockDuration</a>: <i>String</i>
    <a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>: <i>Double</i>
    <a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
    <a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>: <i>Boolean</i>
    <a href="#requiressession" title="RequiresSession">RequiresSession</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### AutoDeleteOnIdle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetteringOnMessageExpiration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMessageTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuplicateDetectionHistoryTimeWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableExpress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePartitioning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeliveryCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeInMegabytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresDuplicateDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresSession

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

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

