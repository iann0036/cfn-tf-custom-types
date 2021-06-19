# TF::Lacework::AlertChannelJiraServer

Configure Lacework to forward events to Jira. Lacework calls the Jira integration REST API and creates a new Jira open issue for each Lacework event that meets or exceeds the specified alert severity level. If there is a large volume of events that exceed the ability of Jira REST API to create new Jira issues, priority is given to those events with the highest severity.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelJiraServer",
    "Properties" : {
        "<a href="#customtemplatefile" title="CustomTemplateFile">CustomTemplateFile</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#groupissuesby" title="GroupIssuesBy">GroupIssuesBy</a>" : <i>String</i>,
        "<a href="#issuetype" title="IssueType">IssueType</a>" : <i>String</i>,
        "<a href="#jiraurl" title="JiraUrl">JiraUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#projectkey" title="ProjectKey">ProjectKey</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelJiraServer
Properties:
    <a href="#customtemplatefile" title="CustomTemplateFile">CustomTemplateFile</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#groupissuesby" title="GroupIssuesBy">GroupIssuesBy</a>: <i>String</i>
    <a href="#issuetype" title="IssueType">IssueType</a>: <i>String</i>
    <a href="#jiraurl" title="JiraUrl">JiraUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#projectkey" title="ProjectKey">ProjectKey</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CustomTemplateFile

A Custom Template JSON file to populate fields in the new Jira issues.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIssuesBy

Defines how Lacework compliance events get grouped. Must be one of `Events` or `Resources`. Defaults to `Events`.
The available options are:
* **Events**:	Single Jira issue will be created when compliance events of the same type but from different resources are detected by Lacework. For example, if three different S3 resources are generating the same compliance event, only one Jira ticket is created.
* **Resources**: Multiple Jira issues will be created when multiple resources are generating the same compliance event. For example, if three different S3 resources are generating the same compliance event, three Jira issues are created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueType

The Jira Issue type (such as a `Bug`) to create when a new Jira issue is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JiraUrl

The URL of your Jira implementation without https protocol (`https://`). For example, `mycompany.atlassian.net` or `mycompany.jira.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password to the Jira user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectKey

The project key for the Jira project where the new Jira issues should be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The Jira user name. Lacework recommends a dedicated Jira user. See above for more information.

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

