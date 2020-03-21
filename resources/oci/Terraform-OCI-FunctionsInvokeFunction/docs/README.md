# Terraform::OCI::FunctionsInvokeFunction

CloudFormation equivalent of oci_functions_invoke_function

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::FunctionsInvokeFunction",
    "Properties" : {
        "<a href="#base64encodecontent" title="Base64EncodeContent">Base64EncodeContent</a>" : <i>Boolean</i>,
        "<a href="#fnintent" title="FnIntent">FnIntent</a>" : <i>String</i>,
        "<a href="#fninvoketype" title="FnInvokeType">FnInvokeType</a>" : <i>String</i>,
        "<a href="#functionid" title="FunctionId">FunctionId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#inputbodysourcepath" title="InputBodySourcePath">InputBodySourcePath</a>" : <i>String</i>,
        "<a href="#invokefunctionbody" title="InvokeFunctionBody">InvokeFunctionBody</a>" : <i>String</i>,
        "<a href="#invokefunctionbodybase64encoded" title="InvokeFunctionBodyBase64Encoded">InvokeFunctionBodyBase64Encoded</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::FunctionsInvokeFunction
Properties:
    <a href="#base64encodecontent" title="Base64EncodeContent">Base64EncodeContent</a>: <i>Boolean</i>
    <a href="#fnintent" title="FnIntent">FnIntent</a>: <i>String</i>
    <a href="#fninvoketype" title="FnInvokeType">FnInvokeType</a>: <i>String</i>
    <a href="#functionid" title="FunctionId">FunctionId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#inputbodysourcepath" title="InputBodySourcePath">InputBodySourcePath</a>: <i>String</i>
    <a href="#invokefunctionbody" title="InvokeFunctionBody">InvokeFunctionBody</a>: <i>String</i>
    <a href="#invokefunctionbodybase64encoded" title="InvokeFunctionBodyBase64Encoded">InvokeFunctionBodyBase64Encoded</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### Base64EncodeContent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FnIntent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FnInvokeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputBodySourcePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvokeFunctionBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvokeFunctionBodyBase64Encoded

_Required_: No

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

#### Content

Returns the &lt;code&gt;Content&lt;/code&gt; value.

#### InvokeEndpoint

Returns the &lt;code&gt;InvokeEndpoint&lt;/code&gt; value.

