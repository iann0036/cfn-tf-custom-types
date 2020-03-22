# Terraform::OCI::FunctionsInvokeFunction

This resource provides the Invoke Function resource in Oracle Cloud Infrastructure Functions service.

Invokes a function

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
        "<a href="#inputbodysourcepath" title="InputBodySourcePath">InputBodySourcePath</a>" : <i>String</i>,
        "<a href="#invokefunctionbody" title="InvokeFunctionBody">InvokeFunctionBody</a>" : <i>String</i>,
        "<a href="#invokefunctionbodybase64encoded" title="InvokeFunctionBodyBase64Encoded">InvokeFunctionBodyBase64Encoded</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
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
    <a href="#inputbodysourcepath" title="InputBodySourcePath">InputBodySourcePath</a>: <i>String</i>
    <a href="#invokefunctionbody" title="InvokeFunctionBody">InvokeFunctionBody</a>: <i>String</i>
    <a href="#invokefunctionbodybase64encoded" title="InvokeFunctionBodyBase64Encoded">InvokeFunctionBodyBase64Encoded</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Base64EncodeContent

Encodes the response returned, if any, in base64. It is recommended to set this to `true` to avoid corrupting the returned response, if any, in Terraform state. The default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FnIntent

An optional intent header that indicates to the FDK the way the event should be interpreted. E.g. 'httprequest', 'cloudevent'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FnInvokeType

Indicates whether the functions platform should execute the request directly and return the result ('sync') or whether the platform should enqueue the request for later processing and acknowledge that it has been processed ('detached').

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputBodySourcePath

An absolute path to a file on the local system that contains the input to be provided to the function. Cannot be defined if `invoke_function_body` or `invoke_function_body_base64_encoded` is defined. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvokeFunctionBody

The body of the function invocation. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit. Cannot be defined if `input_body_source_path` or `invoke_function_body_base64_encoded` is defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvokeFunctionBodyBase64Encoded

The Base64 encoded body of the function invocation. Base64 encoded input avoids corruption in Terraform state. Cannot be defined if `invoke_function_body` or `input_body_source_path` is defined. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Content

Returns the <code>Content</code> value.

#### Id

Returns the <code>Id</code> value.

#### InvokeEndpoint

Returns the <code>InvokeEndpoint</code> value.

