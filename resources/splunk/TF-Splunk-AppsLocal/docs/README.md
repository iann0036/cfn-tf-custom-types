# TF::Splunk::AppsLocal

Create, install and manage apps on your Splunk instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::AppsLocal",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>String</i>,
        "<a href="#author" title="Author">Author</a>" : <i>String</i>,
        "<a href="#configured" title="Configured">Configured</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#explicitappname" title="ExplicitAppname">ExplicitAppname</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>Boolean</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#session" title="Session">Session</a>" : <i>String</i>,
        "<a href="#update" title="Update">Update</a>" : <i>Boolean</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#visible" title="Visible">Visible</a>" : <i>Boolean</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::AppsLocal
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>String</i>
    <a href="#author" title="Author">Author</a>: <i>String</i>
    <a href="#configured" title="Configured">Configured</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#explicitappname" title="ExplicitAppname">ExplicitAppname</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>Boolean</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#session" title="Session">Session</a>: <i>String</i>
    <a href="#update" title="Update">Update</a>: <i>Boolean</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#visible" title="Visible">Visible</a>: <i>Boolean</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### Auth

Splunkbase session token for operations like install and update that require login. Use auth or session when installing or updating an app through Splunkbase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Author

For apps posted to Splunkbase, use your Splunk account username. For internal apps, include your name and contact information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configured

Custom setup complete indication:
<br>true = Custom app setup complete.
<br>false = Custom app setup not complete.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Short app description also displayed below the app title in Splunk Web Launcher.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitAppname

Custom app name. Overrides name when installing an app from a file where filename is set to true. See also filename.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

Indicates whether to use the name value as the app source location.
<br>true indicates that name is a path to a file to install.
<br>false indicates that name is the literal app name and that the app is created from Splunkbase using a template.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

App name displayed in Splunk Web, from five to eighty characters excluding the prefix "Splunk for".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Literal app name or path for the file to install, depending on the value of filename.
<br>filename = false indicates that name is the literal app name and that the app is created from Splunkbase using a template.
<br>filename = true indicates that name is the URL or path to the local .tar, .tgz or .spl file. If name is the Splunkbase URL, set auth or session to authenticate the request.
The app folder name cannot include spaces or special characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Session

Login session token for installing or updating an app on Splunkbase. Alternatively, use auth.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Update

File-based update indication:
<br>true specifies that filename should be used to update an existing app. If not specified, update defaults to
<br>false, which indicates that filename should not be used to update an existing app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

App version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visible

Indicates whether the app is visible and navigable from Splunk Web.
<br>true = App is visible and navigable.
<br>false = App is not visible or navigable.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

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

