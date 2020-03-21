# Terraform::AzureRM::ApplicationGateway RedirectConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#includepath" title="IncludePath">IncludePath</a>" : <i>Boolean</i>,
    "<a href="#includequerystring" title="IncludeQueryString">IncludeQueryString</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#redirecttype" title="RedirectType">RedirectType</a>" : <i>String</i>,
    "<a href="#targetlistenername" title="TargetListenerName">TargetListenerName</a>" : <i>String</i>,
    "<a href="#targeturl" title="TargetUrl">TargetUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#includepath" title="IncludePath">IncludePath</a>: <i>Boolean</i>
<a href="#includequerystring" title="IncludeQueryString">IncludeQueryString</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#redirecttype" title="RedirectType">RedirectType</a>: <i>String</i>
<a href="#targetlistenername" title="TargetListenerName">TargetListenerName</a>: <i>String</i>
<a href="#targeturl" title="TargetUrl">TargetUrl</a>: <i>String</i>
</pre>

## Properties

#### IncludePath

Whether or not to include the path in the redirected Url. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeQueryString

Whether or not to include the query string in the redirected Url. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique name of the redirect configuration block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectType

The type of redirect. Possible values are `Permanent`, `Temporary`, `Found` and `SeeOther`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetListenerName

The name of the listener to redirect to. Cannot be set if `target_url` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetUrl

The Url to redirect the request to. Cannot be set if `target_listener_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

