# TF::Akamai::GtmAsmap

Use the `akamai_gtm_asmap` resource to create, configure, and import a GTM Autonomous System (AS) map. AS mapping lets you configure a GTM property that returns a CNAME based on the AS number associated with the requester's IP address. 

You can reuse maps for multiple properties or create new ones. AS maps split the Internet into multiple AS block zones. Properties that use AS maps can specify handout integers for each zone. AS mapping lets you configure a property that directs users to a specific environment or to the origin. 

~> **Note** Import requires an ID with this format: `existing_domain_name`:`existing_map_name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmAsmap",
    "Properties" : {
        "<a href="#defaultdatacenter" title="DefaultDatacenter">DefaultDatacenter</a>" : <i>[ <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a>, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>,
        "<a href="#assignment" title="Assignment">Assignment</a>" : <i>[ <a href="assignmentdefinition.md">AssignmentDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmAsmap
Properties:
    <a href="#defaultdatacenter" title="DefaultDatacenter">DefaultDatacenter</a>: <i>
      - <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a></i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
    <a href="#assignment" title="Assignment">Assignment</a>: <i>
      - <a href="assignmentdefinition.md">AssignmentDefinition</a></i>
</pre>

## Properties

#### DefaultDatacenter

_Required_: Yes

_Type_: List of <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assignment

_Required_: No

_Type_: List of <a href="assignmentdefinition.md">AssignmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

