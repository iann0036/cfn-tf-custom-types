# TF::Akamai::GtmResource ResourceInstanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>Double</i>,
    "<a href="#loadobject" title="LoadObject">LoadObject</a>" : <i>String</i>,
    "<a href="#loadobjectport" title="LoadObjectPort">LoadObjectPort</a>" : <i>Double</i>,
    "<a href="#loadservers" title="LoadServers">LoadServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#usedefaultloadobject" title="UseDefaultLoadObject">UseDefaultLoadObject</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>Double</i>
<a href="#loadobject" title="LoadObject">LoadObject</a>: <i>String</i>
<a href="#loadobjectport" title="LoadObjectPort">LoadObjectPort</a>: <i>Double</i>
<a href="#loadservers" title="LoadServers">LoadServers</a>: <i>
      - String</i>
<a href="#usedefaultloadobject" title="UseDefaultLoadObject">UseDefaultLoadObject</a>: <i>Boolean</i>
</pre>

## Properties

#### DatacenterId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadObject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadObjectPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultLoadObject

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

