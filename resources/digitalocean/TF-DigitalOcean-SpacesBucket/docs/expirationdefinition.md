# TF::DigitalOcean::SpacesBucket ExpirationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#date" title="Date">Date</a>" : <i>String</i>,
    "<a href="#days" title="Days">Days</a>" : <i>Double</i>,
    "<a href="#expiredobjectdeletemarker" title="ExpiredObjectDeleteMarker">ExpiredObjectDeleteMarker</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#date" title="Date">Date</a>: <i>String</i>
<a href="#days" title="Days">Days</a>: <i>Double</i>
<a href="#expiredobjectdeletemarker" title="ExpiredObjectDeleteMarker">ExpiredObjectDeleteMarker</a>: <i>Boolean</i>
</pre>

## Properties

#### Date

Specifies the date/time after which you want applicable objects to expire. The argument uses
RFC3339 format, e.g. "2020-03-22T15:03:55Z" or parts thereof e.g. "2019-02-28".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Days

Specifies the number of days after object creation when the applicable objects will expire.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiredObjectDeleteMarker

On a versioned bucket (versioning-enabled or versioning-suspended
bucket), setting this to true directs Spaces to delete expired object delete markers.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

