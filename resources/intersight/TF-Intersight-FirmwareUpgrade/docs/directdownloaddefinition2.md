# TF::Intersight::FirmwareUpgrade DirectDownloadDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
    "<a href="#httpserver" title="HttpServer">HttpServer</a>" : <i>[ <a href="directdownloaddefinition.md">DirectDownloadDefinition</a>, ... ]</i>,
    "<a href="#imagesource" title="ImageSource">ImageSource</a>" : <i>String</i>,
    "<a href="#ispasswordset" title="IsPasswordSet">IsPasswordSet</a>" : <i>Boolean</i>,
    "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#upgradeoption" title="Upgradeoption">Upgradeoption</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
<a href="#httpserver" title="HttpServer">HttpServer</a>: <i>
      - <a href="directdownloaddefinition.md">DirectDownloadDefinition</a></i>
<a href="#imagesource" title="ImageSource">ImageSource</a>: <i>String</i>
<a href="#ispasswordset" title="IsPasswordSet">IsPasswordSet</a>: <i>Boolean</i>
<a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#upgradeoption" title="Upgradeoption">Upgradeoption</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServer

_Required_: No

_Type_: List of <a href="directdownloaddefinition.md">DirectDownloadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPasswordSet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upgradeoption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
