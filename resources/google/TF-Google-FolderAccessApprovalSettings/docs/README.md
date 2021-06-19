# TF::Google::FolderAccessApprovalSettings

Access Approval enables you to require your explicit approval whenever Google support and engineering need to access your customer content.


To get more information about FolderSettings, see:

* [API documentation](https://cloud.google.com/access-approval/docs/reference/rest/v1/folders)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::FolderAccessApprovalSettings",
    "Properties" : {
        "<a href="#folderid" title="FolderId">FolderId</a>" : <i>String</i>,
        "<a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#enrolledservices" title="EnrolledServices">EnrolledServices</a>" : <i>[ <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::FolderAccessApprovalSettings
Properties:
    <a href="#folderid" title="FolderId">FolderId</a>: <i>String</i>
    <a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>: <i>
      - String</i>
    <a href="#enrolledservices" title="EnrolledServices">EnrolledServices</a>: <i>
      - <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### FolderId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnrolledServices

_Required_: No

_Type_: List of <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a>

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

#### EnrolledAncestor

Returns the <code>EnrolledAncestor</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

