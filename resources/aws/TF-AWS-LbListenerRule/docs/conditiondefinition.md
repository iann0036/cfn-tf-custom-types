# TF::AWS::LbListenerRule ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>[ <a href="hostheaderdefinition.md">HostHeaderDefinition</a>, ... ]</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>, ... ]</i>,
    "<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>" : <i>[ <a href="httprequestmethoddefinition.md">HttpRequestMethodDefinition</a>, ... ]</i>,
    "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>[ <a href="pathpatterndefinition.md">PathPatternDefinition</a>, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ <a href="querystringdefinition.md">QueryStringDefinition</a>, ... ]</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ <a href="sourceipdefinition.md">SourceIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostheader" title="HostHeader">HostHeader</a>: <i>
      - <a href="hostheaderdefinition.md">HostHeaderDefinition</a></i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="httpheaderdefinition.md">HttpHeaderDefinition</a></i>
<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>: <i>
      - <a href="httprequestmethoddefinition.md">HttpRequestMethodDefinition</a></i>
<a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>
      - <a href="pathpatterndefinition.md">PathPatternDefinition</a></i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>
      - <a href="querystringdefinition.md">QueryStringDefinition</a></i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - <a href="sourceipdefinition.md">SourceIpDefinition</a></i>
</pre>

## Properties

#### HostHeader

_Required_: No

_Type_: List of <a href="hostheaderdefinition.md">HostHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestMethod

_Required_: No

_Type_: List of <a href="httprequestmethoddefinition.md">HttpRequestMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

_Required_: No

_Type_: List of <a href="pathpatterndefinition.md">PathPatternDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of <a href="querystringdefinition.md">QueryStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: List of <a href="sourceipdefinition.md">SourceIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

