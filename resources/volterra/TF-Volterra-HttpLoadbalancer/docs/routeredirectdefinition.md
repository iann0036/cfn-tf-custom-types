# TF::Volterra::HttpLoadbalancer RouteRedirectDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allparams" title="AllParams">AllParams</a>" : <i>Boolean</i>,
    "<a href="#hostredirect" title="HostRedirect">HostRedirect</a>" : <i>String</i>,
    "<a href="#pathredirect" title="PathRedirect">PathRedirect</a>" : <i>String</i>,
    "<a href="#protoredirect" title="ProtoRedirect">ProtoRedirect</a>" : <i>String</i>,
    "<a href="#removeallparams" title="RemoveAllParams">RemoveAllParams</a>" : <i>Boolean</i>,
    "<a href="#responsecode" title="ResponseCode">ResponseCode</a>" : <i>Double</i>,
    "<a href="#retainallparams" title="RetainAllParams">RetainAllParams</a>" : <i>Boolean</i>,
    "<a href="#stripqueryparams" title="StripQueryParams">StripQueryParams</a>" : <i>[ <a href="stripqueryparamsdefinition.md">StripQueryParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allparams" title="AllParams">AllParams</a>: <i>Boolean</i>
<a href="#hostredirect" title="HostRedirect">HostRedirect</a>: <i>String</i>
<a href="#pathredirect" title="PathRedirect">PathRedirect</a>: <i>String</i>
<a href="#protoredirect" title="ProtoRedirect">ProtoRedirect</a>: <i>String</i>
<a href="#removeallparams" title="RemoveAllParams">RemoveAllParams</a>: <i>Boolean</i>
<a href="#responsecode" title="ResponseCode">ResponseCode</a>: <i>Double</i>
<a href="#retainallparams" title="RetainAllParams">RetainAllParams</a>: <i>Boolean</i>
<a href="#stripqueryparams" title="StripQueryParams">StripQueryParams</a>: <i>
      - <a href="stripqueryparamsdefinition.md">StripQueryParamsDefinition</a></i>
</pre>

## Properties

#### AllParams

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRedirect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRedirect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtoRedirect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveAllParams

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainAllParams

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StripQueryParams

_Required_: No

_Type_: List of <a href="stripqueryparamsdefinition.md">StripQueryParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

