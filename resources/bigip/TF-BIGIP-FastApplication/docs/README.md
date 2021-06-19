# TF::BIGIP::FastApplication

`bigip_fast_application` This resource will create and manage FAST applications on BIG-IP from provided JSON declaration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::FastApplication",
    "Properties" : {
        "<a href="#fastjson" title="FastJson">FastJson</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::FastApplication
Properties:
    <a href="#fastjson" title="FastJson">FastJson</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### FastJson

Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.

_Required_: No

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

#### Application

A FAST application name.

#### Id

Returns the <code>Id</code> value.

#### Tenant

A FAST tenant name on which you want to manage application.

