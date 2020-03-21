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

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeQueryString

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetListenerName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetUrl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

