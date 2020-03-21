# Terraform::AWS::IotThing

CloudFormation equivalent of aws_iot_thing

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IotThing",
    "Properties" : {
        "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ &lt;a href=&#34;attributes.md&#34;&gt;Attributes&lt;/a&gt;, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#thingtypename" title="ThingTypeName">ThingTypeName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IotThing
Properties:
    <a href="#attributes" title="Attributes">Attributes</a>: <i>
      - &lt;a href=&#34;attributes.md&#34;&gt;Attributes&lt;/a&gt;</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#thingtypename" title="ThingTypeName">ThingTypeName</a>: <i>String</i>
</pre>

## Properties

#### Attributes

_Required_: No

_Type_: List of &lt;a href=&#34;attributes.md&#34;&gt;Attributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThingTypeName

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

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### DefaultClientId

Returns the &lt;code&gt;DefaultClientId&lt;/code&gt; value.

#### Version

Returns the &lt;code&gt;Version&lt;/code&gt; value.

