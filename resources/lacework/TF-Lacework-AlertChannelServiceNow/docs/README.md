# TF::Lacework::AlertChannelServiceNow

You can configure Lacework to forward alerts to Service Now using the ServiceNow REST API.

To find more information see the [Lacework support documentation](https://support.lacework.com/hc/en-us/articles/360005842314-ServiceNow).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelServiceNow",
    "Properties" : {
        "<a href="#customtemplatefile" title="CustomTemplateFile">CustomTemplateFile</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#instanceurl" title="InstanceUrl">InstanceUrl</a>" : <i>String</i>,
        "<a href="#issuegrouping" title="IssueGrouping">IssueGrouping</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelServiceNow
Properties:
    <a href="#customtemplatefile" title="CustomTemplateFile">CustomTemplateFile</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#instanceurl" title="InstanceUrl">InstanceUrl</a>: <i>String</i>
    <a href="#issuegrouping" title="IssueGrouping">IssueGrouping</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CustomTemplateFile

Populate fields in the ServiceNow incident with values from a custom template JSON file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceUrl

The ServiceNow instance URL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueGrouping

Defines how Lacework compliance events get grouped. Must be one of `Events` or `Resources`. Defaults to `Events`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The ServiceNow password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The ServiceNow user name.

_Required_: Yes

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

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.

